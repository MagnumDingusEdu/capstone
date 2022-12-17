import "bootstrap/dist/css/bootstrap.min.css";
import "./assets/index.css";
import MeritCombinedForm from "./components/MeritCombinedForm";

const App = () => {
  return (
    <div className="App">
      <div className="d-flex flex-column h-100">
        <main className="flex-shrink-0">
          <div className="container">
            <h1 className="mt-5">Autogrant Merit-I & Merit-II</h1>
            <MeritCombinedForm />
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;
