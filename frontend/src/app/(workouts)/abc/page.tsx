"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";

type AbcItems = {
  id: number;
  lletra: string;
  numbro: number;
  voice: string;
  vocals: string;
};

function Abc() {
  const [abcItem, setAbcItem] = useState<AbcItems[]>([]);

  const getUsers = async () => {
    const red = await axios.get(process.env.BASE_URL + `/abc/item`);
    //console.log(red.data.abc_item);
    setAbcItem(red.data.abc_item);
  };

  useEffect(() => {
    //console.log(localStorage.getItem("user"));
    getUsers();
  }, []);

  return (
    <div>
      <div className="grid grid-cols-4 gap-4">
        {abcItem.map((abc) => (
          <div
            key={abc.id}
            className="flux max-w-sm rounded overflow-hidden shadow-lg"
          >
            {abc.lletra}

            {abc.vocals}
            {abc.voice}

            <audio controls>
              <source
                id="audio-player"
                name="audio-player"
                src={abc.voice}
                type="audio/mp3"
              />
              {/* Fallback content */}
              Your browser does not support the audio element.
            </audio>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Abc;
