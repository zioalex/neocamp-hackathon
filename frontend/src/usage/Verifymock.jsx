import React, { Component } from 'react';
import api from "../utils/api"

class Verifymock extends Component {
  constructor(props) {
    super(props)
    this.state = {
      image: true,
      list: []

    }
    this.handleImgClick = this.handleImgClick.bind(this)
    this.handleButtClick = this.handleButtClick.bind(this)
    this.handleFault = this.handleFault.bind(this);
  }
  componentDidMount() {
    //check backend/blockchain to receive data
    api
      .get()//address
      .then(data => {
        this.setState({
          list: data,
        })
      })
      .catch(err => {
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

  handleFault() {
    //submit update to the blockchain- to change ownership of NFT for repair, removal, modification

  }

  render() {
    if (this.state.image) {
      return (
        <div>
          <img className="splash-img" onClick={this.handleImgClick} src={require("../assets/plane-info.png")} alt="landing" width="70%" />
        </div>
      );
    }
    else {
      return (
        <div className="verify">
          <div className="data">
            <button className="back-button" onClick={this.handleButtClick}>{"< Back"}</button>
            <div className="simple-flex">
              <div className="item-name">Aircraft C-BASE15: Landing Gear
              </div><button onClick={this.handleFault}>Report Fault</button>
            </div>
            <div>
              <img className="item-img" src={require("../assets/gear.png")} alt="item" />
            </div>
            <table>
              <tr>
              <td className="t-key">Part Name</td>
              <td>Landing Gear</td>
              </tr>
              <tr>
              <td className="t-key">Serial Number</td>
              <td>GH6426ERI12N</td>
              </tr>
              <tr>
              <td className="t-key">Current Status</td>
              <td>Ok</td>
              </tr>
              <tr>
              <td className="t-key">Manufacture Date</td>
              <td>18-09-17</td>
              </tr>
              <tr>
              <td className="t-key">Weight</td>
              <td>100kg</td>
              </tr>
              <tr>
              <td className="t-key">Speed</td>
              <td>over 300km/h</td>
              </tr>
              <tr>
              <td className="t-key">Rolling Distance</td>
              <td>up to 500.000 km</td>
              </tr>
              <tr>
              <td className="t-key">Life Time Of</td>
              <td>60.000 / 20 years</td>
              </tr>
              <tr>
              <td className="t-key">In-Service Cycle</td>
              <td>20.000 (overhaul)</td>
              </tr>
            
            </table>
          </div>

          <div className="timeline">
            <div className="time-point">
              <div className="vert-icon">
                <div className="vert-line">
                  <div> <img src={require("../assets/circleicon.png")} alt="icon" width="30px" />
                  </div>
                </div>
              </div><div>
                <div>20 Aug 2018, 11:18</div>
                <div className="timeline-block">Landing Gear GH6426ERI12N was registered by James Sudo</div>
              </div>
            </div>
            <div className="time-point">
              <div className="vert-icon">
                <div className="vert-line">
                  <div> <img src={require("../assets/circleicon.png")} alt="icon" width="30px" />
                  </div>
                </div>
              </div><div>
                <div>22 Aug 2018, 22:32</div>
                <div className="timeline-block">Landing Gear installed in airplane</div>
              </div>
            </div>
            <div className="time-point">
              <div className="vert-icon">
                <div className="vert-line">
                  <div> <img src={require("../assets/circleicon.png")} alt="icon" width="30px" />
                  </div>
                </div>
              </div><div>
                <div>24 Aug 2018, 10:42</div>
                <div className="timeline-block">Landing Gear Broken</div>
              </div>
            </div>
          </div>
        </div >
      )
    }
  }
}

export default Verifymock;