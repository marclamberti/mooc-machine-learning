function [error_test] = validationTest(X, y, Xtest, ytest, lambda)

theta = trainLinearReg(X, y, lambda);
error_test = sum((Xtest * theta - ytest) .^ 2) / (2 * size(Xtest, 1));

end