"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";

type Silabaun = {
  id: number;
  nom: string;
  order: number;
  silabaun_id: string;
};

function Silabaun() {
  const [silabaun, setSilabaun] = useState<Silabaun[]>([]);

  const getUsers = async () => {
    const red = await axios.get(`http://localhost:4000/silabaun`);
    console.log(red.data.silabaun);
    setSilabaun(red.data.silabaun);
  };

  useEffect(() => {
    //console.log(localStorage.getItem("user"));
    getUsers();
  }, []);

  return (
    <div>
      {silabaun.map((sil) => (
        <div key={sil.id}>{sil.nom} </div>
      ))}
    </div>
  );
}

export default Silabaun;
