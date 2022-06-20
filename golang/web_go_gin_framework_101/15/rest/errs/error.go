package errs

import "net/http"

type AppErrs struct {
	Code    int
	Message string
}

func NewNotFoundError() *AppErrs {
	return &AppErrs{
		Code:    http.StatusNotFound,
		Message: "Not Found",
	}
}

func NewServerError(msg string) *AppErrs {
	return &AppErrs{
		Code:    http.StatusInternalServerError,
		Message: msg,
	}
}
