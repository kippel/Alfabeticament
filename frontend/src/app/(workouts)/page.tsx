"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";

import AbcPage from "../(workouts)/AbcPage";

type Abc = {
  id: number;
  abc: string;
  icon: string;
  href: string;
};

function WorkoutsPage() {
  const [abc, setAbc] = useState<Abc[]>([]);

  //console.log(process.env.BASE_URL);

  const getUsers = async () => {
    const red = await axios.get(process.env.BASE_URL + `/abc`);
    //console.log(red.data.abc);
    setAbc(red.data.abc);
  };

  useEffect(() => {
    //console.log(localStorage.getItem("user"));
    getUsers();
  }, []);

  return (
    <div>
      <div className="grid grid-cols-4 gap-4">
        {abc.map((abc) => (
          <AbcPage abc={abc} key={abc.id} />
        ))}
      </div>
    </div>
  );
}

export default WorkoutsPage;
