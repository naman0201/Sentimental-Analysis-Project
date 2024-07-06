/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */

import React, { Component, useState } from 'react'

const Login2 = (props) => {
  const [count, setCount] = useState(props.count)
  return (
    <>
      <div>Hello</div>
      <button
        onClick={() => {
          setCount(count + 1)
        }}
      >
        Click Me
      </button>
      <h1>{count}</h1>
    </>
  )
}
export default Login2
