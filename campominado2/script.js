document.addEventListener('DOMContentLoaded', () => {

    // --- CONTROLE DE NAVEGAÇÃO E ESTADO GERAL ---
    const paginas = document.querySelectorAll('.pagina');
    let modoSelecionado = null;
    let jogoAtual = null;

    // Função central para trocar de tela
    function mostrarPagina(idPagina) {
        paginas.forEach(p => p.classList.remove('ativa'));
        document.getElementById(idPagina).classList.add('ativa');
    }

    // --- LÓGICA DO JOGO (CLASSE CampoMinado) ---
    class CampoMinado {
        constructor(modo) {
            const [linhas, cols] = modo.split('x').map(Number);
            this.linhas = linhas;
            this.cols = cols;
            this.totalCelulas = this.linhas * this.cols;
            this.numMinas = Math.floor(this.totalCelulas * 0.2); // Minas são 20% do total de células

            // Elementos do HTML que o jogo vai controlar
            this.tabuleiroElement = document.getElementById('tabuleiro');
            this.infoPontosElement = document.getElementById('info-pontos');
            this.infoTempoElement = document.getElementById('info-tempo');
            
            // Estado interno do jogo
            this.modelo = []; // Onde a lógica do tabuleiro (bombas, números) é guardada
            this.jogoAtivo = true;
            this.pontos = 0;
            this.celulasReveladas = 0;
            this.maxPontos = this.totalCelulas - this.numMinas;
            this.tempoInicio = null;
            this.intervaloTempo = null;
        }

        iniciar() {
            this.criarModeloLogico();
            this.renderizarTabuleiroNaTela();
            this.tempoInicio = Date.now();
            this.intervaloTempo = setInterval(() => this.atualizarTempo(), 1000);
            this.infoPontosElement.textContent = `0/${this.maxPontos}`;
        }

        // A LÓGICA DINÂMICA que funciona para qualquer tamanho de tabuleiro
        criarModeloLogico() {
            // 1. Cria um tabuleiro 2D (array de arrays) vazio, cheio de objetos
            this.modelo = Array.from({ length: this.linhas }, () => 
                Array.from({ length: this.cols }, () => ({ temBomba: false, revelada: false, bandeira: false, vizinhos: 0 }))
            );

            // 2. Planta as minas em posições aleatórias
            let minasPlantadas = 0;
            while (minasPlantadas < this.numMinas) {
                const l = Math.floor(Math.random() * this.linhas);
                const c = Math.floor(Math.random() * this.cols);
                if (!this.modelo[l][c].temBomba) {
                    this.modelo[l][c].temBomba = true;
                    minasPlantadas++;
                }
            }

            // 3. Para cada célula, calcula quantas bombas vizinhas ela tem
            for (let l = 0; l < this.linhas; l++) {
                for (let c = 0; c < this.cols; c++) {
                    if (this.modelo[l][c].temBomba) continue;
                    
                    let contagem = 0;
                    // Este loop duplo varre os 8 vizinhos ao redor da célula (l, c)
                    for (let i = -1; i <= 1; i++) {
                        for (let j = -1; j <= 1; j++) {
                            const vizinhoL = l + i;
                            const vizinhoC = c + j;
                            // Verifica se o vizinho está dentro dos limites do tabuleiro
                            if (vizinhoL >= 0 && vizinhoL < this.linhas && vizinhoC >= 0 && vizinhoC < this.cols) {
                                if (this.modelo[vizinhoL][vizinhoC].temBomba) {
                                    contagem++;
                                }
                            }
                        }
                    }
                    this.modelo[l][c].vizinhos = contagem;
                }
            }
        }

        renderizarTabuleiroNaTela() {
            this.tabuleiroElement.innerHTML = '';
            this.tabuleiroElement.style.gridTemplateColumns = `repeat(${this.cols}, 35px)`;
            
            for (let l = 0; l < this.linhas; l++) {
                for (let c = 0; c < this.cols; c++) {
                    const celula = document.createElement('div');
                    celula.classList.add('celula');
                    celula.dataset.linha = l;
                    celula.dataset.coluna = c;

                    celula.addEventListener('click', () => this.cliqueEsquerdo(l, c));
                    celula.addEventListener('contextmenu', (e) => {
                        e.preventDefault();
                        this.cliqueDireito(l, c);
                    });
                    this.tabuleiroElement.appendChild(celula);
                }
            }
        }
        
        atualizarVisualDaCelula(l, c) {
            const celulaElement = this.tabuleiroElement.querySelector(`[data-linha='${l}'][data-coluna='${c}']`);
            const celulaModelo = this.modelo[l][c];

            celulaElement.className = 'celula'; // Reseta o estilo

            if(celulaModelo.bandeira) {
                celulaElement.classList.add('bandeira');
            }

            if (celulaModelo.revelada) {
                celulaElement.classList.add('revelada');
                if (celulaModelo.temBomba) {
                    celulaElement.classList.add('bomba');
                    celulaElement.textContent = '💣';
                } else if (celulaModelo.vizinhos > 0) {
                    celulaElement.textContent = celulaModelo.vizinhos;
                }
            }
        }

        cliqueEsquerdo(l, c) {
            if (!this.jogoAtivo || this.modelo[l][c].revelada || this.modelo[l][c].bandeira) return;

            const celulaModelo = this.modelo[l][c];
            celulaModelo.revelada = true;
            
            if (celulaModelo.temBomba) {
                this.fimDeJogo(false);
                return;
            }
            
            this.celulasReveladas++;
            this.pontos++;
            this.infoPontosElement.textContent = `${this.pontos}/${this.maxPontos}`;
            this.atualizarVisualDaCelula(l, c);

            // Se clicou em uma célula com 0 vizinhos, revela as adjacentes
            if (celulaModelo.vizinhos === 0) {
                this.revelarVizinhos(l, c);
            }

            // Verifica condição de vitória
            if (this.celulasReveladas === this.maxPontos) {
                this.fimDeJogo(true);
            }
        }
        
        cliqueDireito(l, c) {
            if (!this.jogoAtivo || this.modelo[l][c].revelada) return;
            const celulaModelo = this.modelo[l][c];
            celulaModelo.bandeira = !celulaModelo.bandeira;
            this.atualizarVisualDaCelula(l, c);
        }
        
        // Revela em cascata
        revelarVizinhos(l, c) {
             for (let i = -1; i <= 1; i++) {
                for (let j = -1; j <= 1; j++) {
                    const vizinhoL = l + i;
                    const vizinhoC = c + j;
                    if (vizinhoL >= 0 && vizinhoL < this.linhas && vizinhoC >= 0 && vizinhoC < this.cols) {
                        // Chama o clique normal no vizinho, que tem suas próprias checagens
                        this.cliqueEsquerdo(vizinhoL, vizinhoC);
                    }
                }
            }
        }
        
        atualizarTempo() {
            const segundos = Math.floor((Date.now() - this.tempoInicio) / 1000);
            this.infoTempoElement.textContent = `${segundos}s`;
        }
        
        fimDeJogo(vitoria) {
            this.jogoAtivo = false;
            clearInterval(this.intervaloTempo);
            const duracao = Math.floor((Date.now() - this.tempoInicio) / 1000);

            if (vitoria) {
                alert("Você venceu!");
                salvarPartida(this.pontos, this.maxPontos, duracao);
            } else {
                alert("Você perdeu!");
                this.modelo.forEach((linha, l) => linha.forEach((celula, c) => {
                    if (celula.temBomba) {
                        celula.revelada = true;
                        this.atualizarVisualDaCelula(l, c);
                    }
                }));
            }
        }
    }

    // --- LÓGICA DO HISTÓRICO (Usa o localStorage do navegador) ---
    function salvarPartida(pontos, maxPontos, duracao) {
        const historico = JSON.parse(localStorage.getItem('historicoCampoMinado')) || [];
        historico.push({ data: new Date().toISOString(), pontos, maxPontos, duracao });
        localStorage.setItem('historicoCampoMinado', JSON.stringify(historico));
    }

    function formatarDataRelativa(dataISO) {
        const agora = new Date();
        const dataPartida = new Date(dataISO);
        const diffSegundos = Math.floor((agora - dataPartida) / 1000);
        const diffDias = Math.floor(diffSegundos / 86400);

        if (diffDias === 0) return `hoje, às ${dataPartida.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })}`;
        if (diffDias === 1) return 'ontem';
        if (diffDias < 7) return `há ${diffDias} dias`;
        if (diffDias < 14) return 'há 1 semana';
        if (diffDias < 30) return `há ${Math.floor(diffDias / 7)} semanas`;
        if (diffDias < 60) return 'há 1 mês';
        if (diffDias < 365) return `há ${Math.floor(diffDias / 30)} meses`;
        return `há ${Math.floor(diffDias / 365)} anos`;
    }

    function renderizarHistorico() {
        const historico = JSON.parse(localStorage.getItem('historicoCampoMinado')) || [];
        const container = document.getElementById('lista-historico');
        container.innerHTML = '';

        if (historico.length === 0) {
            container.textContent = 'Nenhuma partida jogada ainda.';
            return;
        }

        historico.sort((a, b) => new Date(b.data) - new Date(a.data));

        historico.forEach(partida => {
            const item = document.createElement('div');
            item.classList.add('item-historico');
            item.innerHTML = `
                <strong>${formatarDataRelativa(partida.data)}</strong><br>
                Pontuação: ${partida.pontos}/${partida.maxPontos}<br>
                Duração: ${partida.duracao} segundos
            `;
            container.appendChild(item);
        });
    }
    
    // --- EVENT LISTENERS (Ligando os botões às ações) ---
    document.body.addEventListener('keydown', () => {
        if (document.getElementById('pagina-inicial').classList.contains('ativa')) {
            mostrarPagina('pagina-menu');
        }
    }, { once: true });
    
    document.getElementById('btn-comecar').addEventListener('click', () => mostrarPagina('pagina-modos'));
    document.getElementById('btn-historico').addEventListener('click', () => {
        renderizarHistorico();
        mostrarPagina('pagina-historico');
    });
    document.querySelectorAll('.btn-voltar').forEach(btn => btn.addEventListener('click', () => mostrarPagina('pagina-menu')));
    
    document.querySelectorAll('.btn-modo').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.btn-modo').forEach(b => b.classList.remove('selecionado'));
            btn.classList.add('selecionado');
            modoSelecionado = btn.dataset.modo;
            document.getElementById('btn-play').disabled = false;
        });
    });

    document.getElementById('btn-play').addEventListener('click', () => {
        if (modoSelecionado) {
            jogoAtual = new CampoMinado(modoSelecionado);
            jogoAtual.iniciar();
            mostrarPagina('pagina-jogo');
        }
    });
});