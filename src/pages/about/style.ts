import { styled } from "styled-components"

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
`;


export const Title = styled.h1`
    font-size: 2rem;
    color: #333;
    margin-bottom: 20px;
`;

export const Content = styled.div`
    font-size: 1rem;
    color: #555;
    line-height: 1.6;
`;

export const Link = styled.a`
    color: #007bff;
    text-decoration: none;
    
    &:hover {
        text-decoration: underline;
    }
`;

export const Recommendation = styled.p`
    margin-top: 20px;
    font-size: 1rem;
    color: #666;
`;
