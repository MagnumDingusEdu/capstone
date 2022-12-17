import PropTypes from "prop-types";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";

import { useState, useEffect } from "react";

const MeritCombinedTable = (props) => {
  const getInitialStudentState = () => {};

  const [studentData, setStudentData] = useState([]);
  const [branchData, setBranchData] = useState([]);

  // second param is empty array so it (hopefully) executes only on first render
  useEffect(() => {
    let rawData = window.x;

    // add default selectionType
    for (let studentId in rawData.students) {
      // one of UNSELECTED, MERIT1, MERIT2, DISQUALIFIED
      rawData.students[studentId].selectionType = "UNSELECTED";
    }

    // sort by marks then AGPA
    rawData.students.sort((a, b) => {
      if (a.marks === b.marks) {
        return b.agpa - a.agpa;
      }
      return b.marks - a.marks;
    });

    // console.log("effectlog", rawData.students);

    setBranchData(rawData.branches);
    setStudentData(rawData.students);
  }, []);

  let studentRows = (
    <>
      {studentData.map((student, index) => (
        <tr>
          <td>{index+1}</td>
          <td>{student.branch}</td>
          <td>{student.reg_no}</td>
          <td>{student.old_reg}</td>
          <td>{student.previous_prog}</td>
          <td>{student.previous_branch}</td>
          <td>{student.studentname}</td>
          <td>{student.quota}</td>
          <td>{student.backlogs}</td>
          <td>{student.agpa}</td>
          <td>{student.marks}</td>
          <td>{student.remarks}</td>
          <td>
            <Button variant="primary">Disqualify</Button>
          </td>
        </tr>
      ))}
    </>
  );

  return (
    <>
      <Table bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Branch</th>
            <th>Reg No</th>
            <th>Old Reg</th>
            <th>Previous Program</th>
            <th>Previous Branch</th>
            <th>Student Name</th>
            <th>Quota</th>
            <th>Backlogs</th>
            <th>AGPA</th>
            <th>Marks</th>
            <th>Remarks</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>{studentRows}</tbody>
      </Table>
    </>
  );
};

export default MeritCombinedTable;
