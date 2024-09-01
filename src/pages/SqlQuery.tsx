import { isAxiosError } from 'axios';
import React, { useState } from 'react';
import api from '../api/api';
import { Button, Container, FormSql, Pre, TextArea, Title } from './style';

const SqlQuery: React.FC = () => {
    const [query, setQuery] = useState<string>('');
    const [response, setResponse] = useState<string>('');

    const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setQuery(event.target.value);
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        try {
            const res = await api.get('/query', { params: { query } });
            setResponse(res.data.replace(/\n/g, '\n'));
        } catch (error) {
            if (isAxiosError(error)) {
                if (error.response) {
                    setResponse(`Error: ${error.response.data}`);
                    if (error.response.data === "no results to fetch") setResponse(`Engraçadinho você em, só aceitamos SELECT`);
                    return
                }
            }
            setResponse(`Error: ${error}`)
        }
    };

    return (
        <Container>
            <h1>SQL</h1>
            <FormSql onSubmit={handleSubmit}>
                <TextArea
                    value={query}
                    onChange={handleInputChange}
                    rows={10}
                    cols={50}
                    placeholder="Escreva sua consulta SQL"
                />
                <Button type="submit">Executar Query</Button>
            </FormSql>
            <Title>Resultado</Title>
            <Pre>{response}</Pre>
        </Container>
    );
};

export default SqlQuery;
