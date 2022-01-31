from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, SubmitField
from wtforms.fields import DateField
from wtforms.validators import DataRequired, NumberRange, Optional


class WeightGoalCalculatorForm(FlaskForm):
    curr_weight = FloatField('Current Weight',
                             validators=[DataRequired(),
                                         NumberRange(min=20, max=300)],
                             render_kw={'unit': 'kg'})
    curr_height = FloatField('Current Height',
                             validators=[DataRequired(),
                                         NumberRange(min=80, max=240)],
                             render_kw={'unit': 'cm'})
    birth_date = DateField('Birth Date', validators=[DataRequired()])
    act_level = SelectField('Activity Level',
                            coerce=float,
                            choices=[(1.2, 'Sedentary'),
                                     (1.375, 'Light Activity'),
                                     (1.55, 'Moderate Activity'),
                                     (1.725, 'Intense Activity'),
                                     (1.9, 'Elite Athlete')],
                            validators=[DataRequired()])
    goal_weight = FloatField('Goal Weight',
                             validators=[DataRequired(),
                                         NumberRange(min=20, max=300)],
                             render_kw={'unit': 'kg'})
    at_time = DateField('Exactly On', validators=[DataRequired()])
    pred_height = FloatField('Predicted Height',
                             validators=[DataRequired(),
                                         NumberRange(min=80, max=240)],
                             render_kw={'unit': 'cm'})
    submit = SubmitField('Calculate')


class BodyAttrCalculatorForm(FlaskForm):
    height = FloatField('Height', validators=[DataRequired(),
                                              NumberRange(min=80, max=240)],
                        render_kw={'unit': 'cm'})
    wrist = FloatField('Wrist', validators=[DataRequired(),
                                            NumberRange(min=8, max=32)],
                       render_kw={'unit': 'cm'})
    chest = FloatField('Chest', validators=[DataRequired(),
                                            NumberRange(min=30, max=200)],
                       render_kw={'unit': 'cm'})
    biceps = FloatField('Biceps (Flexed)',
                        validators=[DataRequired(),
                                    NumberRange(min=15, max=60)],
                        render_kw={'unit': 'cm'})
    thigh = FloatField('Thigh (Flexed)',
                       validators=[DataRequired(),
                                   NumberRange(min=30, max=100)],
                       render_kw={'unit': 'cm'})
    calf = FloatField('Calf (Flexed)',
                      validators=[DataRequired(), NumberRange(min=15, max=60)],
                      render_kw={'unit': 'cm'})
    waist = FloatField('Waist', validators=[DataRequired(),
                                            NumberRange(min=25, max=125)],
                       render_kw={'unit': 'cm'})
    neck = FloatField('Neck', validators=[DataRequired(),
                                          NumberRange(min=32, max=102)],
                      render_kw={'unit': 'cm'})
    hips = FloatField('Hips', validators=[DataRequired(),
                                          NumberRange(min=26, max=170)],
                      render_kw={'unit': 'cm'})
    shoulder = FloatField('Shoulder',
                          validators=[DataRequired(),
                                      NumberRange(min=40, max=200)],
                          render_kw={'unit': 'cm'})
    submit = SubmitField('Calculate')


class BodyFatCalculatorForm(FlaskForm):
    height = FloatField('Height', validators=[DataRequired(),
                                              NumberRange(min=80, max=240)],
                        render_kw={'unit': 'cm'})
    navel = FloatField('Navel', validators=[DataRequired(),
                                            NumberRange(min=30, max=200)],
                       render_kw={'unit': 'cm'})
    neck = FloatField('Neck', validators=[DataRequired(),
                                          NumberRange(min=18, max=80)],
                      render_kw={'unit': 'cm'})
    weight = FloatField('Weight', validators=[NumberRange(min=20, max=300),
                                              Optional()],
                        render_kw={'unit': 'kg'})
    submit = SubmitField('Calculate')


class CircExpCalculatorForm(FlaskForm):
    init_weight = FloatField('Initial Weight',
                             validators=[DataRequired(),
                                         NumberRange(min=20, max=300)],
                             render_kw={'unit': 'kg'})
    init_circ = FloatField('Initial Circumference',
                           validators=[DataRequired(),
                                       NumberRange(min=1, max=200)],
                           render_kw={'unit': 'cm'})
    goal_weight = FloatField('Goal Weight',
                             validators=[DataRequired(),
                                         NumberRange(min=20, max=300)],
                             render_kw={'unit': 'kg'})
    goal_circ = FloatField('Goal Circumference',
                           validators=[DataRequired(),
                                       NumberRange(min=1, max=200)],
                           render_kw={'unit': 'cm'})
    curr_weight = FloatField('Current Weight',
                             validators=[DataRequired(),
                                         NumberRange(min=20, max=300)],
                             render_kw={'unit': 'kg'})
    submit = SubmitField('Calculate')


class AbsPowerCalculatorForm(FlaskForm):
    weight = FloatField('Weight',
                        validators=[DataRequired(),
                                    NumberRange(min=20, max=300)],
                        render_kw={'unit': 'kg'})
    vertical_jump = FloatField('Vertical Jump',
                               validators=[DataRequired(),
                                           NumberRange(min=0, max=100)],
                               render_kw={'unit': 'cm'})
    submit = SubmitField('Calculate')
