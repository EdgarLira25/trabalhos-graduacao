import { styled } from "styled-components"

export const HeaderContainer = styled.header`
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: left;
      padding: 20px 30px;
      border-bottom: 2px solid #dce0e8;
`;

export const Button = styled.button`
  background-color: #dce0e8;
  color: #333;
  margin-right: 10px;
  cursor: pointer;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);

  &:active {
    background-color: #b0b5c3;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }
`;

export const Navegate = styled.nav`
`

export const Title = styled.a`
    font-size: 19px; /* Tamanho da fonte */
    font-weight: bold; /* Peso da fonte */
    letter-spacing: 1px; /* Espaçamento entre letras */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Sombra do texto */
    border-radius: 10px;
    background: linear-gradient(90deg,#04a5e5, #7287fd); /* Gradiente de fundo */
    color: transparent; /* Faz o texto transparente para mostrar o gradiente */
    border: 1px solid rgba(0, 0, 0, 0.1); /* Borda leve */
    padding: 5px; /* Espaçamento interno */
    color: #333; /* Cor do texto */
    margin-right: 15px; /* Margem direita */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
`;
