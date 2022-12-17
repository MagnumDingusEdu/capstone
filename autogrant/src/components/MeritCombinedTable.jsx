import PropTypes from "prop-types";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";

import { useState, useEffect } from "react";

const MeritCombinedTable = (props) => {
  const [studentData, setStudentData] = useState([]);
  const [branchData, setBranchData] = useState([]);

  // second param is empty array so it (hopefully) executes only on first render
  useEffect(() => {
    let rawData = window.x;

    // sort by marks then AGPA
    rawData.students.sort((a, b) => {
      if (a.marks === b.marks) {
        return b.agpa - a.agpa;
      }
      return b.marks - a.marks;
    });

    // add default meritType
    chooseMeritTypes(rawData.students);

    setBranchData(rawData.branches);
    setStudentData(rawData.students);
  }, []);

  useEffect(() => {
    console.debug("New render");
  });

  const chooseMeritTypes = (students) => {
    // assume everything is sorted already

    let leftoverMerit1 = props.totalMerit1;
    let leftoverMerit2 = props.totalMerit2;

    for (let studentId in students) {
      // one of UNSELECTED, MERIT1, MERIT2, DISQUALIFIED
      if (students[studentId].meritType == "DISQUALIFIED") {
        continue;
      } else if (leftoverMerit1 > 0) {
        leftoverMerit1 -= 1;
        students[studentId].meritType = "MERIT1";
      } else if (leftoverMerit2 > 0) {
        leftoverMerit2 -= 1;
        students[studentId].meritType = "MERIT2";
      } else {
        students[studentId].meritType = "UNSELECTED";
      }
    }
  };

  const toggleQualificationStudent = (studentId) => {
    let tmp = [...studentData];

    if (tmp[studentId].meritType == "DISQUALIFIED") {
      tmp[studentId].meritType = "UNSELECTED";
    } else {
      tmp[studentId].meritType = "DISQUALIFIED";
    }

    chooseMeritTypes(tmp);
    setStudentData(tmp);

    // Dunno why this doesnt work

    // setStudentData((prevState) => {
    //   let newState = [...prevState];
    //   console.log("Prev", newState[studentId].meritType);
    //   if (newState[studentId].meritType == "DISQUALIFIED") {
    //     console.log("IF triggered");
    //     newState[studentId].meritType = "UNSELECTED";
    //   } else {
    //     console.log("else triggered");
    //     newState[studentId].meritType = "DISQUALIFIED";
    //   }
    //   console.log("Updated", newState[studentId].meritType);

    //   // newState[studentId].meritType = "DISQUALIFIED";

    //   // now we have to re-choose all merit types
    //   chooseMeritTypes(newState);
    //   console.log("Updated 2", newState[studentId].meritType);
    //   console.log("New State should be", newState);

    //   return newState;
    // });
  };

  const chooseRowBackground = (meritType) => {
    switch (meritType) {
      case "MERIT1":
        return "table-primary";
      case "MERIT2":
        return "table-success";
      case "DISQUALIFIED":
        return "table-danger";
      default:
        return "";
    }
  };

  let studentRows = (
    <>
      {studentData.map((student, index) => (
        <tr
          className={chooseRowBackground(student.meritType)}
          key={index + "student-row"}
        >
          <td>{index + 1}</td>
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
            <Button
              variant="primary"
              onClick={() => toggleQualificationStudent(index)}
            >
              {student.meritType != "DISQUALIFIED"
                ? "Disqualify"
                : "Reconsider"}
            </Button>
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

MeritCombinedTable.defaultProps = {
  totalMerit1: 2,
  totalMerit2: 1,
};

MeritCombinedTable.propTypes = {
  totalMerit1: PropTypes.number,
  totalMerit2: PropTypes.number,
};

export default MeritCombinedTable;
