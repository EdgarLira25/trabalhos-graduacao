import { styled } from "styled-components"

export const HeaderContainer = styled.header`
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      padding: 20px 30px;
      transition: background-color 0.3s ease
`;

export const Title = styled.h1`
    cursor: pointer;
    margin: 0;
`   

export const Button = styled.button`
  background-color: #dce0e8;
  color: #333;
  cursor: pointer;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);

  &:hover {
    background-color: #c3c8d6;
    box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
  }

  &:active {
    background-color: #b0b5c3;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    transform: translateY(0);
  }
`; 

export const Navegate = styled.nav`
`
