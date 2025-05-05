"use client";
import Link from "next/link";
import Image from "next/image";

function AbcPage({ abc }) {
  return (
    <div className="max-w-sm rounded overflow-hidden shadow-lg">
      <Link href={abc.href}>
        <Image
          className="w-full"
          src={abc.icon}
          width={200}
          height={200}
          alt="Picture of the author"
        />
      </Link>
    </div>
  );
}

export default AbcPage;
