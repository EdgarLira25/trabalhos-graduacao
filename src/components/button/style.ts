import styled from 'styled-components'

export const Button = styled.button`
  margin-top: 10px;
  padding: 12px 24px;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  background-color: #1e66f5;

  &:active {
    background-color: #7287fd;
  }

  display: flex;
  align-items: center;
  justify-content: center;

  .spinner {
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-top: 4px solid #fff;
    border-radius: 50%;
    width: 16px;
    height: 16px;
    animation: spin 1s linear infinite;
    margin-left: 8px;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`;
