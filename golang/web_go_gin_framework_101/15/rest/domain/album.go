package domain

import "github.com/monitor-cmr/web-w-go/errs"

type Album struct {
	ID     int
	Title  string
	Artist string
	Price  float64
}

type AlbumRepository interface {
	SelectAll() ([]Album, *errs.AppErrs)
	Select(int) (*Album, *errs.AppErrs)
	Save(Album) (*int, *errs.AppErrs)
	Update(Album) *errs.AppErrs
	Delete(int) *errs.AppErrs
}