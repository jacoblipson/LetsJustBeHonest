var data = [
  {id: 1, first_name: "Pete", text: "This is one comment"},
  {id: 2, first_name: "Jordan", text: "This is *another* comment"}
];

var Politician = React.createClass({
  render: function() {
    return (<div>Name: {this.props.first_name}</div>);
  }
});

var PoliticiansList = React.createClass({
  getInitialState: function() {
      return {data: []};
  },
  componentDidMount: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    var politicianListings = this.state.data.map(function(politician) {
        return (
          <Politician first_name={politician.first_name} />
        );
      });
    return (<div className="politiciansListing">{politicianListings}</div>);
  }
});

var App = React.createClass({
  render: function() {
    return(
      <PoliticiansList url='/api/politicians/list/' />
    );
  }
});

ReactDOM.render(<App />, document.getElementById('app'));
