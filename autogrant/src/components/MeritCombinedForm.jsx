import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { useState } from "react";
import MeritCombinedTable from "./MeritCombinedTable";
import Alert from "react-bootstrap/Alert";

const MeritCombinedForm = (props) => {
  const [totalMerit1, setTotalMerit1] = useState(0);
  const [totalMerit2, setTotalMerit2] = useState(0);
  const [showTable, setShowTable] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  if (!showTable) {
    return (
      <div>
        {showAlert ? <Alert variant="danger">Please input positive integers.</Alert> : ""}
        <Form>
          <Form.Group className="mb-3" controlId="formTotalMerit1">
            <Form.Label>Number of Merit-I scholarships</Form.Label>
            <Form.Control
              type="text"
              placeholder="Ex: 5"
              onChange={(e) => {
                setTotalMerit1(e.target.value);
              }}
            />
          </Form.Group>
          <Form.Group className="mb-3" controlId="formTotalMerit2">
            <Form.Label>Number of Merit-II scholarships</Form.Label>
            <Form.Control
              type="text"
              placeholder="Ex: 5"
              onChange={(e) => {
                setTotalMerit2(e.target.value);
              }}
            />
          </Form.Group>
          <br />
          <br />
          <Button
            variant="primary"
            onClick={() => {
              if (
                Number.isFinite(Number(totalMerit1)) &&
                Number.isFinite(Number(totalMerit2)) &&
                totalMerit1 > 0 &&
                totalMerit2 > 0
              ) {
                console.log("Valid inputs");
                setShowAlert(false);
                setShowTable(true);
              } else {
                console.log("Invalid inputs");
                setShowAlert(true);
              }
            }}
          >
            Calculate
          </Button>
        </Form>
      </div>
    );
  }

  return (
    <>
      <Button
        variant="secondary"
        onClick={() => {
          setShowAlert(false);
          setTotalMerit1(0);
          setTotalMerit2(0);

          setShowTable(false);
        }}
      >
        Reset
      </Button>

      <br />
      <br />

      <MeritCombinedTable totalMerit1={Number(totalMerit1)} totalMerit2={Number(totalMerit2)} />
    </>
  );
};

export default MeritCombinedForm;
