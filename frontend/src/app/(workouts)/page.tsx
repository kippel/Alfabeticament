"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";

type Silaba = {
  id: number;
  silaba: string;
};

function WorkoutsPage() {
  const [silaba, setSilaba] = useState<Silaba[]>([]);

  const getUsers = async () => {
    const red = await axios.get(`http://localhost:4000/silaba`);
    console.log(red.data.silaba);
    setSilaba(red.data.silaba);
  };

  useEffect(() => {
    //console.log(localStorage.getItem("user"));
    getUsers();
  }, []);

  return (
    <div>
      {silaba.map((sil) => (
        <h1 key="{sil.id}">{sil.silaba}</h1>
      ))}
    </div>
  );
}

export default WorkoutsPage;
