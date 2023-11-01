import React from 'react';

const MyPage = ({ data }) => (
  <div>
    <p>{data.someValue}</p>
  </div>
);

export async function getServerSideProps() {
  // Fetch data on the server
  const response = await fetch('file:///D:/pytemp/src/pages/pages/response/index.js');
  const data = await response.json();

  return {
    props: {
      data,
    },
  };
}

export default MyPage;
