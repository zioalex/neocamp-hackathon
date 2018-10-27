import React, { Component } from 'react';

class Verify extends Component {
  constructor(props) {
    super(props)
    this.state = {
      image: true,

    }
    this.handleImgClick = this.handleImgClick.bind(this)
    this.handleButtClick = this.handleButtClick.bind(this)
  }

  handleImgClick() {
    this.setState({
      image: false
    })
  }
  handleButtClick() {
    this.setState({
      image: true
    })
  }
  componentDidMount() {
    //check backend/blockchain to receive data
  }
  render() {
    if (this.state.image) {
      return (
        <div>
          <img onClick={this.handleImgClick} src={require("../assets/plane-info.png")} alt="landing" width="100%" />
        </div>
      );
    }
    else {
      return (
        <div className="verify">
          <div className="data">
            data column
            <br/>
            <button onClick={this.handleButtClick}>Back</button>

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