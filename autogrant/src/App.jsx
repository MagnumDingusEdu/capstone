import "bootstrap/dist/css/bootstrap.min.css";
import "./assets/index.css";
import { useState } from "react";
import Example from "./components/Example";

const App = () => {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <div className="d-flex flex-column h-100">
        <main className="flex-shrink-0">
          <div className="container">
            <h1 className="mt-5">Autogrant Scholarship Test</h1>
            <p className="lead">Some BS lorem ipsum type crap here.</p>
            <Example title="Fucko"></Example>
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;
