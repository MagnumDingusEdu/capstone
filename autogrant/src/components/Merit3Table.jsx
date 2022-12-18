import PropTypes from "prop-types";
import Table from "react-bootstrap/Table";
import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";

import Button from "react-bootstrap/Button";

import { useState, useEffect } from "react";

const Merit3Table = (props) => {
  const [studentData, setStudentData] = useState({});
  const [branchData, setBranchData] = useState({});

  // second param is empty array so it (hopefully) executes only on first render
  useEffect(() => {
    let rawData = window.m3;

    let branches = Object.keys(rawData.branches);

    // for every branch, sort by marks then AGPA
    for (let branch in rawData.students) {
      rawData.students[branch].sort((a, b) => {
        if (a.marks === b.marks) {
          return b.agpa - a.agpa;
        }
        return b.marks - a.marks;
      });
    }

    // add default meritTypes for every branch

    for (let branch in rawData.students) {
      let branchStrength = rawData.branches[branch].strength;
      chooseMeritTypes(rawData.students[branch], branchStrength);
    }

    setBranchData(rawData.branches);
    setStudentData(rawData.students);
  }, []);

  useEffect(() => {
    console.debug("New render");
  });

  const chooseMeritTypes = (branchStudents, branchStrength) => {
    let leftover = Math.floor((branchStrength * props.totalPercentage) / 100);

    for (let studentId in branchStudents) {
      // one of UNSELECTED, MERIT3, DISQUALIFIED
      if (branchStudents[studentId].meritType == "DISQUALIFIED") {
        continue;
      } else if (leftover > 0) {
        leftover -= 1;
        branchStudents[studentId].meritType = "MERIT3";
      } else {
        branchStudents[studentId].meritType = "UNSELECTED";
      }
    }
  };

  const toggleQualificationStudent = (studentIndex, branch) => {
    // this disqualifies or reconsiders a student from scholarships

    let tmp = { ...studentData };

    if (tmp[branch][studentIndex].meritType == "DISQUALIFIED") {
      tmp[branch][studentIndex].meritType = "UNSELECTED";
    } else {
      tmp[branch][studentIndex].meritType = "DISQUALIFIED";
    }

    // only re-choose merit types for particular this branch
    chooseMeritTypes(tmp[branch], branchData[branch].strength);

    setStudentData(tmp);
  };

  const chooseRowBackground = (meritType) => {
    switch (meritType) {
      case "MERIT3":
        return "table-success";
      case "DISQUALIFIED":
        return "table-danger";
      default:
        return "";
    }
  };

  return (
    <>
      <div class="btn-group" role="group">
        <button type="button" class="btn btn-success" disabled>
          Merit Scholarship III
        </button>
        <button type="button" class="btn btn-danger" disabled>
          Disqualified
        </button>
      </div>
      <br />

      <Tabs id="student-branch-tabs" className="mb-3" fill>
        {Object.keys(studentData).map((branch, branchIndex) => (
          <Tab
            eventKey={branchIndex}
            title={branch}
            key={branchIndex + "branch-tab"}
          >
            <h3>Branch:</h3>

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
              <tbody>
                {studentData[branch].map((student, studentIndex) => (
                  <tr
                    className={chooseRowBackground(student.meritType)}
                    key={studentIndex + "branch-student-row"}
                  >
                    <td>{studentIndex + 1}</td>
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
                        onClick={() =>
                          toggleQualificationStudent(studentIndex, branch)
                        }
                      >
                        {student.meritType != "DISQUALIFIED"
                          ? "Disqualify"
                          : "Reconsider"}
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </Tab>
        ))}
      </Tabs>
    </>
  );
};

Merit3Table.defaultProps = {
  totalPercentage: 10,
};

Merit3Table.propTypes = {
  totalPercentage: PropTypes.number,
};

export default Merit3Table;
