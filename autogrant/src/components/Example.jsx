import React from "react";
import PropTypes from "prop-types";
import Accordion from "react-bootstrap/Accordion";
import Button from "react-bootstrap/Button";
import { useState } from "react";

const Example = (props) => {
  const [count, setCount] = useState(0);

  const doSomething = () => {
    console.log(window.x);
    setCount(count + 1);
  };

  return (
    <div>
      <h3>{props.title}</h3>
      <p>Pressed {count} times.</p>
      <Button variant="primary" onClick={doSomething}>
        Click Me
      </Button>
    </div>
  );
};

Example.defaultProps = {
  title: "Lol Wat",
};

Example.propTypes = {
  title: PropTypes.string,
};

export default Example;
