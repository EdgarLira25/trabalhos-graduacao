import { useNavigate } from 'react-router-dom';
import { Button, HeaderContainer, Navegate, Title } from './style';

const Header = () => {
    const navigate = useNavigate();

    const handleNavigateHome = () => {
        navigate('/query');
    };
    const handleNavigateTables = () => {
        navigate('/tables');
    };

    const handleNavigateExamples = () => {
        navigate('/examples');
    };

    const handleNavigateAbout = () => {
        navigate('/about')
    }

    return (
        <HeaderContainer>
            <Title href="https://edisciplinas.usp.br/course/view.php?id=124198" target="_blank" >ACH2004 - BD1</Title>
            <Navegate>
                <Button onClick={handleNavigateHome}>
                    Realizar Consulta
                </Button>
                <Button onClick={handleNavigateExamples}>
                    Exemplos de Queries
                </Button>
                <Button onClick={handleNavigateTables}>
                    Tabelas do Database
                </Button>
                <Button onClick={handleNavigateAbout}>
                    Sobre
                </Button>
            </Navegate>
        </HeaderContainer >
    );
};

export default Header;
