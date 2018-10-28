import React, { Component } from 'react';
import './styles/App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Navigation from './Navigation'
import Home from './Home'
import Register from './usage/Register'
import Repair from './usage/Repair'
import Verify from './usage/Verifymock'   //using mockup for presentation
import NotFound from './NotFound'
// import Auth from './Auth'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      user: null
    }
  }

  render() {
    return (
      < BrowserRouter >
        <div>
          <Navigation user={this.state.user} />
          <Switch>
            <Route exact path="/" render={() => <Home user={this.state.user} />} />
            <Route exact path="/register" render={() => <Register user={this.state.user} />} />
            <Route exact path="/repair" render={() => <Repair user={this.state.user} />} />
            <Route exact path="/verify" render={() => <Verify user={this.state.user} />} />
            {/* <Route
              path="/auth"
              render={() => <Auth setUser={this._setUser} resetUser={this._resetUser} />}
            /> */}
            <Route component={NotFound} />
          </Switch>
        </div>
      </BrowserRouter >
    );
  }
}

export default App;
