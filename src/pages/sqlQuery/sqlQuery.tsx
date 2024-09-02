import { isAxiosError } from 'axios';
import React, { useState } from 'react';
import api from '../../api/api';
import LoadingButton from '../../components/button/button';
import { Container, FormSql, Pre, TextArea } from './style';

const SqlQuery: React.FC = () => {
    const [query, setQuery] = useState<string>('');
    const [response, setResponse] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false)
    const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setQuery(event.target.value);
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setIsLoading(true)
        try {
            const res = await api.get('/query', { params: { query } });
            setResponse(res.data.replace(/\n/g, '\n'));
        } catch (error) {
            if (isAxiosError(error)) {
                if (error.response) {
                    setResponse(`Error: ${error.response.data}`);
                    if (error.response.data === "no results to fetch") setResponse(`só aceitamos SELECT`);
                }
            }
            else {
                setResponse(`Error: ${error}`)
            }
        }
        setIsLoading(false)
    };

    return (
        <Container>
            <h1>Escreva sua Consulta SQL</h1>
            <FormSql onSubmit={handleSubmit}>
                <TextArea
                    value={query}
                    onChange={handleInputChange}
                    rows={10}
                    cols={50}
                />
                <LoadingButton loading={isLoading}>Executar Consulta</LoadingButton>
            </FormSql>
            <Pre>{response}</Pre>
        </Container>
    );
};

export default SqlQuery;
