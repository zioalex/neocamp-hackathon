import React from 'react'
import { Link } from 'react-router-dom'

const Navigation = props => {
  return (

    <div className="navigation">
     
        <div>
        <Link className="link logo" to="/">
        <img src={require("./assets/Logo.svg")} width="150px" alt="PartChain"/>
                    </Link>
      </div>

      <div>
        <Link className="link" to="/Register">
          Register
                            </Link>
      </div>
      <div>
        <Link className="link" to="Verify">
          Verify
                            </Link>
      </div>
    </div>
  )
}

export default Navigation
