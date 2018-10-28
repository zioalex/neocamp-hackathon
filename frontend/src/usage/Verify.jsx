import React, { Component } from 'react';
import api from "../utils/api"

class Verify extends Component {
  constructor(props) {
    super(props)
    this.state = {
      image: true,
      list:[]

    }
    this.handleImgClick = this.handleImgClick.bind(this)
    this.handleButtClick = this.handleButtClick.bind(this)
  }
componentDidMount(){
   //check backend/blockchain to receive data
  api
  .get()//address
  .then(data=>{
    this.setState({
      list:data,
    })
  })
  .catch(err=>{
    console.log(err);
  })
}

  handleImgClick() {
    this.setState({
      image: false
    })
    //in real usage this should call the backend/blockchain based on chosen component
  }
  handleButtClick() {
    this.setState({
      image: true
    })
  }
 
  render() {
    if (this.state.image) {
      return (
        <div>
          <img className="splash-img"onClick={this.handleImgClick} src={require("../assets/plane-info.png")} alt="landing" width="100%" />
        </div>
      );
    }
    else {
      return (
        <div className="verify">
          <div className="data">
            <button className="back-button" onClick={this.handleButtClick}>{"< Back"}</button>
<div>

</div>
          </div>
          <div className="timeline">
            timeline column
</div>
        </div>
      )
    }
  }
}

export default Verify;