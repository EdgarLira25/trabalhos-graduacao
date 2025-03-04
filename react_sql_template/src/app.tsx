import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/header/header';
import About from './pages/about/about';
import ExamplesQueries from './pages/examplesQueries/examplesQueries';
import SqlQuery from './pages/sqlQuery/sqlQuery';
import Tabelas from './pages/tabelas/tabelas';

function App() {
    return (
        <Router>
            <Header></Header>
            <Routes>
                <Route path="/" element={<Navigate to="/query" />} />
                <Route path="/query" element={<SqlQuery />} />
                <Route path="/tables" element={<Tabelas />} />
                <Route path="/examples" element={<ExamplesQueries />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </Router>
    );
}

export default App;
