var Politician = React.createClass({
  displayName: 'Politician',

  render: function () {
    return React.createElement(
      'div',
      null,
      'Name: ',
      this.props.first_name,
      ', HonestyScore: ',
      this.props.honesty_score
    );
  }
});

var PoliticiansList = React.createClass({
  displayName: 'PoliticiansList',

  getInitialState: function () {
    return { data: [] };
  },
  componentDidMount: function () {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      success: function (data) {
        this.setState({ data: data });
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  render: function () {
    var politicianListings = this.state.data.map(function (politician) {
      return React.createElement(Politician, { first_name: politician.first_name, honesty_score: politician.honesty_score });
    });
    return React.createElement(
      'div',
      { className: 'politiciansListing' },
      politicianListings
    );
  }
});

var App = React.createClass({
  displayName: 'App',

  render: function () {
    return React.createElement(PoliticiansList, { url: '/api/politicians/list/' });
  }
});

ReactDOM.render(React.createElement(App, null), document.getElementById('app'));