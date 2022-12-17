import React from "react";
import ReactDOM from "react-dom/client";
import MeritCombinedForm from "./components/MeritCombinedForm";
import Merit3Form from "./components/Merit3Form";

// import "bootstrap/dist/css/bootstrap.min.css"; // remove this if using template bootstrap
import "./assets/index.css";

ReactDOM.createRoot(document.getElementById("root-m12")).render(
  <React.StrictMode>
    <>
      <h1 className="mt-5">Autogrant Merit-I & Merit-II</h1>
      <MeritCombinedForm />
    </>
  </React.StrictMode>
);

ReactDOM.createRoot(document.getElementById("root-m3")).render(
  <React.StrictMode>
    <>
      <h1 className="mt-5">Autogrant Merit-III</h1>
      <Merit3Form />
    </>
  </React.StrictMode>
);
