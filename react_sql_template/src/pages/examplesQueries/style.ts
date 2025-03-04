import { styled } from "styled-components"

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
`;

export const Title = styled.h1``

export const ContainerList = styled.div`
  max-height: 650px;
  overflow-y: auto;
  padding: 10px;
`

export const ContainerItem = styled.div`
  display: flex;
  alignItems: center;
  margin-bottom: 20px;
`

export const Pre = styled.pre`
 background-color: #f4f4f4;
 padding: 10px;
 border-radius: 5px;
 margin: 0;
 word-wrap: break-word;
 flex: 1
`
