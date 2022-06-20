package domain

type Album struct {
	ID     int
	Title  string
	Artist string
	Price  float64
}

type AlbumRepository interface {
	SelectAll() ([]Album, error)
	Select(int) (*Album, error)
	Save(Album) (*int, error)
	Update(Album) error
	Delete(int) error
}