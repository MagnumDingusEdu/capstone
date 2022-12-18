import React from "react";

import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { useState } from "react";
import Alert from "react-bootstrap/Alert";
import Merit3Table from "./Merit3Table";

const Merit3Form = (props) => {
  const [totalPercentage, setTotalPercentage] = useState(0);
  const [showTable, setShowTable] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  if (!showTable) {
    return (
      <div>
        {showAlert ? (
          <Alert variant="danger">Please input a positive integer which is less-than/equal-to 100.</Alert>
        ) : (
          ""
        )}
        <Form>
          <Form.Group className="mb-3" controlId="formTotalPercentage">
            <Form.Label>
              Percentage of students per branch who should get Merit-III
              scholarships
            </Form.Label>
            <Form.Control
              type="text"
              placeholder="Ex: 15"
              onChange={(e) => {
                setTotalPercentage(e.target.value);
              }}
            />
          </Form.Group>

          <br />
          <Button
            variant="primary"
            onClick={() => {
              if (
                Number.isFinite(Number(totalPercentage)) &&
                totalPercentage > 0 &&
                totalPercentage <= 100
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
          setTotalPercentage(0);

          setShowTable(false);
        }}
      >
        Reset
      </Button>

      <br />
      <br />

      <Merit3Table totalPercentage={Number(totalPercentage)} />
    </>
  );
};

export default Merit3Form;
