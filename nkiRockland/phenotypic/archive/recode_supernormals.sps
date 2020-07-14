* Encoding: UTF-8.
DO IF  (RANGE(AutomaticallycalculatedAGE,65,69)).
RECODE DelayTotalCorrect (13.55 thru Highest=1) INTO supernormal.
END IF.
EXECUTE.



USE ALL.
COMPUTE filter_$=(RANGE(AutomaticallycalculatedAGE,65,69)).
VARIABLE LABELS filter_$ 'RANGE(AutomaticallycalculatedAGE,65,69) (FILTER)'.
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
FORMATS filter_$ (f1.0).
FILTER BY filter_$.
RECODE DelayTotalCorrect (13.55 thru Highest=1) INTO supernormal.
EXECUTE.
