import PropTypes from "prop-types";
import Accordion from "react-bootstrap/Accordion";
import Button from "react-bootstrap/Button";

const Example = (props) => {
  return (
    <div>
      <h3>{props.title}</h3>
      <Button variant="primary">Click Me</Button>
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
