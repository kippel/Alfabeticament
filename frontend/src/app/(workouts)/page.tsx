"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";
import Link from "next/link";

type Silaba = {
  id: number;
  silaba: string;
  silaba_id: string;
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
        <div key="{sil.id}">
          {sil.silaba}
          <Link href={sil.silaba_id}>{sil.silaba_id}</Link>
        </div>
      ))}
    </div>
  );
}

export default WorkoutsPage;
