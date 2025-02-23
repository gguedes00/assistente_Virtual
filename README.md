# Assistente Virtual Inteligente 🤖
[![DIO](https://img.shields.io/badge/Made%20at-DIO-%230A0A0A?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6QUM1QzFDQTdENEFFMTFFQ0JBNkVDOTRERTA2N0U2Q0IiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6QUM1QzFDQThENEFFMTFFQ0JBNkVDOTRERTA2N0U2Q0IiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpBQzVDMUNBNUQ0QUUxMUVDQkE2RUM5NERFMDY3RTZDQiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpBQzVDMUNBNkQ0QUUxMUVDQkE2RUM5NERFMDY3RTZDQiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PqNW4kEAAAFUSURBVHjajJI9aBNhGMafu0vS5GKM0aQfVUFBxEVBxE1BcRBB6uLk4CDi4uDg5CQ4iIO4iOCiDk6Kg6CIgyCC4CQo1EEQpK0WjU1zm+SSu8vHvZdc0lwv4QMv7/vc+zzv+3HvKaVSCQzDqKPR6D3btu8HvV6vR6vV4l8Ih8PwPA+O4yAej5+o1+sPqQcHBwcIBoMIhULwff+/gBACnudhMBggFoudrNVqD6jpdBrj8Rjdbheu6/4VkFJKgFqtBiklMpnMqWq1ep+az+dlv9+XjUZDttttORqNpOu6cjKZSGqj0ZDValXWarV5Px6P5fnz5+Xm5qY8d+6cPHv2rLxy5Yrc2tqS1FwuJzOZjEyn0zKZTMpoNCqjkcg8Qz0ej8vBYCC3t7fl3t6e3N3dlTs7O3J/f1/SNzY2ZCqVkqurq3JlZUUuLS1JwzCkruvSMA1qgM1mUzLDMDAajTAcDkHf3t6GaZowTRO2bcOyrPlM0zRomgZN16EG+OnTp1/3CQQCWF5exsrKCkzLguM4oHPmM4IzmQxM0wQzVB0Oh3N4NpthNpthOp1iPB5D0XUdtm1DURQwQ9UB/AB5MBHZxYODDQAAAABJRU5ErkJggg==)](https://www.dio.me/)
[![Licença MIT](https://img.shields.io/badge/Licença-MIT-green.svg)](LICENSE)

Projeto desenvolvido durante o Bootcamp da Digital Innovation One, integrando tecnologias de voz e tradução automática.

## 🌟 Recursos Principais

### Assistente por Voz

- **Controle vocal** para abertura de sites
- Integração com plataformas de educação (DIO)
- Sistema de feedback por áudio
- Interface colorida no terminal

### Tradutor Inteligente

- Tradução **PT ↔ EN** em tempo real
- Entrada por voz ou texto
- Síntese vocal com vozes nativas
- Sistema de validação de conteúdo
- Gerenciamento de arquivos de áudio

## 🛠 Tecnologias Utilizadas

| Ferramenta          | Função                               |
|---------------------|--------------------------------------|
| `pyttsx3`           | Síntese de voz                       |
| `speech_recognition`| Reconhecimento de fala               |
| `googletrans`       | Tradução automática                  |
| `pygame`            | Reprodução de áudio                  |
| `colorama`          | Formatação de terminal colorido      |


## 📂 Estrutura do Projeto

bootcamp-dio/
├── assistente.py # Assistente principal
├── voice_text_translator.py # Módulo de tradução
├── requirements.txt # Dependências
└── translations/ # Arquivos de áudio gerados


## 🚀 Como Executar

1. **Clonar repositório**
   

git clone https://github.com/gguedes00/assistente_Virtual.git
cd bootcamp-dio
Instalar dependências


pip install -r requirements.txt

Executar módulos


# Assistente Virtual
python assistente.py

# Tradutor Inteligente
python voice_text_translator.py



📄 Licença
Este projeto está sob licença MIT - veja LICENSE para detalhes.

Developed with ❤️ by Gabriel Guedes
Bootcamp: BairesDev - Machine Learning Practitioner, na Digital Innovation One
