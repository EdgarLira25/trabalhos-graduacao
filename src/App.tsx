import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/header';
import ExamplesQueries from './pages/ExamplesQueries/ExamplesQueries';
import SqlQuery from './pages/SqlQuery/SqlQuery';
import Tabelas from './pages/Tabelas/Tabelas';

function App() {
    return (
        <Router>
            <Header></Header>
            <Routes>
                <Route path="/" element={<Navigate to="/query" />} />
                <Route path="/query" element={<SqlQuery />} />
                <Route path="/tables" element={<Tabelas />} />
                <Route path="/examples" element={<ExamplesQueries />} />
            </Routes>
        </Router>
    );
}

export default App;
