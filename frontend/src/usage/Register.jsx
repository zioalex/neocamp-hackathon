import React, {Component} from 'react';

class Register extends Component {
  constructor(props) {
    super(props)

    this.state = {
      Serial_number: "",
      Part_name: "",
      TechSpec: "",
      Manufacture_date: "",
      Lifespan: "",
      Current_status: ""
    }
  

    this.handleInputChange = this.handleInputChange.bind(this);
  }


handleInputChange(event) {
  const target = event.target;
  const value = target.value;
  const name = target.name;

  this.setState({
    [name]: value
  });
}

handleSubmit(event){
  event.preventDefault();


}

  render(){
    return (
      <div className="inputForm">
        <form onSubmit={this.handleSubmit}>
          <label>
            Serial Number <br />
            <input
              name="Serial_number"
              type="text"
              value={this.state.Serial_number}
              onChange={this.handleInputChange} />
          </label>
          <br />
          <label>
            Part Name <br />
            <input
              name="Part_name"
              type="text"
              value={this.state.Part_name}
              onChange={this.handleInputChange} />
          </label>
          <br />
          <label>
            TechSpec<br />
            <input
              name="TechSpec"
              type="text"
              value={this.state.TechSpec}
              onChange={this.handleInputChange} />
          </label>
          <br/>
          <label>
            Manufacture Date <br />
            <input
              name="Manufacture_date"
              type="text"
              value={this.state.Manufacture_date}
              onChange={this.handleInputChange} />
          </label>
          <br/>
          <label>
            Lifespan <br />
            <input
              name="Lifespan"
              type="text"
              value={this.state.Lifespan}
              onChange={this.handleInputChange} />
          </label>
          <label>
            <br/>
            Current Status <br />
            <input
              name="Current_status"
              type="text"
              value={this.state.Current_status}
              onChange={this.handleInputChange} />
          </label>
          <br/>
          <br/>
          <input type="submit" value="Submit" />

        </form>
      </div>
    );
  };
}
  export default Register;