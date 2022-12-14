import React from "react";
import ReactDOM from "react-dom/client";
import MeritCombinedForm from "./components/MeritCombinedForm";
import Merit3Form from "./components/Merit3Form";

// import "bootstrap/dist/css/bootstrap.min.css"; // remove this if using template bootstrap
// import "./assets/index.css";

const merit12Node = document.getElementById("root-m12");
const merit3Node = document.getElementById("root-m3");

if (merit12Node) {
  ReactDOM.createRoot(document.getElementById("root-m12")).render(
    <React.StrictMode>
      <>
        <MeritCombinedForm />
      </>
    </React.StrictMode>
  );
}

if (merit3Node) {
  ReactDOM.createRoot(document.getElementById("root-m3")).render(
    <React.StrictMode>
      <>
        <Merit3Form />
      </>
    </React.StrictMode>
  );
}
