import { styled } from "styled-components"


export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
`;

export const TextArea = styled.textarea`
  padding: 12px;
  border: 2px solid #dce0e8;
  border-radius: 8px;
  background-color: #f2f4f8;
  font-size: 16px;
  line-height: 1.5;
`;

export const Title = styled.h2`
  font-size: 28px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
  text-align: center;
  border-bottom: 2px solid #dce0e8;
  padding-bottom: 10px;
`;

export const Pre = styled.pre`
    margin-top:20px;
`;

export const FormSql = styled.form`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`
