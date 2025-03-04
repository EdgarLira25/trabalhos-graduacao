import React from 'react';
import { Container, Negrito, TextField } from './style';

const Tabelas: React.FC = () => {
    return (
        <Container>
            <h1>Movies Database</h1>
            <TextField>
                - As <span style={{ color: 'green' }}>setas verdes</span> indicam as chaves primárias da tabela (Repare que algumas são compostas)
            </TextField>
            <TextField>
                - <Negrito>Losangulos</Negrito> indicam chave estrangeira:
                Ex: movie_id da tabela <Negrito>has_alternative</Negrito> é chave estrangeira de movie_id da tabela <Negrito>movies</Negrito>
            </TextField>
            <img src="./assets/diagrama.png" alt="Diagrama do Banco de Dados" />
        </Container>
    );
};

export default Tabelas;
