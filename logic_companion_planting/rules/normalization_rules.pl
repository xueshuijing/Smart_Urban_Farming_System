% logic_companion_planting/rules/normalization_rules.pl

% =========================================================
% NORMALIZATION RULES
% =========================================================

normalize(X, Canonical) :-
    alias(X, Canonical).

normalize(X, X) :-
    \+ alias(X, _).
