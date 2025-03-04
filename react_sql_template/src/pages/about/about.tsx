import 'react-toastify/dist/ReactToastify.css';
import { Container, Title, Content, Link, Recommendation } from './style';

const About = () => {
    return (
        <Container>
            <Title>Sobre/Recomendações</Title>
            <Content>
                Recomendação:
                <Recommendation>
                    <ul>
                    <li>
                       Entendam as consultas presentes neste <Link href="https://www.cl.cam.ac.uk/teaching/2021/Databases/relational-tutorial.html" target="_blank" rel="noopener noreferrer">Link</Link> e tentem replicar. OBS: Não será possível replicar as Create View.
                    </li>
                    </ul>
                </Recommendation>
                Recomendações Extras:
                <Recommendation>
                    <ul>
                        <li>
                            Instalem o PostgreSQL em suas máquinas e tentem criar tabelas, realizar selects e etc. Pode poupar tempo mais adiante na época das provas.
                        </li>
                        <li>
                            Vejam essa classe de conexão com o Database <Link href="https://github.com/EdgarLiraa/flask_api_template/blob/main/services/database/manager.py" target="_blank" rel="noopener noreferrer">Conector Python</Link>. Pode ser uma inspiração quando estiverem fazendo uma para o trabalho de vocês.
                        </li>
                    </ul>
                </Recommendation>
                Ferramentas de conexão direta com o PostgreSQL:
                <Recommendation>
                    <ul>
                        <li> Simples e leve: <Link href="https://www.beekeeperstudio.io/" target="_blank" rel="noopener noreferrer">Beekeeper-Studio</Link>
                        </li>
                        <li>
                            Completa e robusta: <Link href="https://www.pgadmin.org/download/" target="_blank" rel="noopener noreferrer">pgAdmin</Link>

                        </li>
                    </ul>
                </Recommendation>
                Email para contato:
                <Recommendation>
                    <ul>
                        <li>
                            Professora: proliveira@usp.br
                        </li>
                        <li>
                            Monitor: edgar.lira@usp.br
                        </li>
                    </ul>
                </Recommendation>
                <p>Códigos Fonte Desta Página:</p>
                <ul>
                    <li>
                        <Link href="https://github.com/EdgarLiraa/react_sql_template" target="_blank" rel="noopener noreferrer">
                            Frontend (React)
                        </Link>
                    </li>
                    <li>
                        <Link href="https://github.com/EdgarLiraa/flask_api_template" target="_blank" rel="noopener noreferrer">
                            Backend (Flask)
                        </Link>
                    </li>
                    <li>
                    <Link href="https://github.com/EdgarLiraa/flask_api_template/blob/main/pg_dump.zip" target="_blank" rel="noopener noreferrer">Script de Criação do DB (PostgreSQL 16.3)</Link>

                    </li>
                </ul>

            </Content>
        </Container>
    );
};

export default About;
