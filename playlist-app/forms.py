"""Forms for playlist app."""

from wtforms import SelectField, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    artist = StringField('Artist', validators=[DataRequired(), Length(max=100)])
    length = IntegerField('Length (minutes)', validators=[DataRequired(), NumberRange(min=1)])

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
