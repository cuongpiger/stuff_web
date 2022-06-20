package mysql

import (
	"database/sql"
	"fmt"

	"github.com/monitor-cmr/web-w-go/domain"
	"github.com/monitor-cmr/web-w-go/errs"
)

type AlbumMySQL struct {
	db *sql.DB
}

func NewAlbumMySQL(db *sql.DB) *AlbumMySQL {
	return &AlbumMySQL{
		db: db,
	}
}

func (a *AlbumMySQL) SelectAll() ([]domain.Album, *errs.AppErrs) {
	sqlstmt := "SELECT id, title, artist, price FROM albums"
	rows, err := a.db.Query(sqlstmt)

	if err != nil {
		fmt.Println("Cannot connect to SQL Server.")
		return nil, errs.NewServerError("Server Internal Error")
	}

	var (
		record = domain.Album{}
		albums = []domain.Album{}
	)

	for rows.Next() {
		err := rows.Scan(&record.ID, &record.Title, &record.Artist, &record.Price)
		if err != nil {
			fmt.Println("Cannot scan row.")
			return nil, errs.NewServerError("Server Internal Error")
		}

		albums = append(albums, record)
	}

	return albums, nil
}

func (a *AlbumMySQL) Select(id int) (*domain.Album, *errs.AppErrs) {
	var record = domain.Album{}

	sqlstmt := "SELECT id, title, artist, price FROM albums WHERE id = ?"
	err := a.db.QueryRow(sqlstmt, id).Scan(&record.ID, &record.Title, &record.Artist, &record.Price)

	if err != nil {
		if err == sql.ErrNoRows {
			fmt.Println("No rows found.", err.Error())
			return nil, errs.NewNotFoundError()
		}

		fmt.Println("Server Scanning Row Error.", err.Error())
		return nil, errs.NewServerError("Server Internal Error")
	}

	return &record, nil
}

func (a *AlbumMySQL) Save(album domain.Album) (*int, *errs.AppErrs) {
	sqlstmt := "INSERT INTO albums (title, artist, price) VALUES (?, ?, ?)"
	result, err := a.db.Exec(sqlstmt, album.Title, album.Artist, album.Price)

	if err != nil {
		fmt.Println("Can not connect to SQL Server.", err.Error())
		return nil, errs.NewServerError("Server Internal Error")
	}

	id, err := result.LastInsertId()
	if err != nil {
		fmt.Println("Server Get RowID Error.", err.Error())
		return nil, errs.NewServerError("Server Internal Error")
	}

	resultID := int(id) // cobvert int64 to int
	return &resultID, nil
}

func (a *AlbumMySQL) Update(album domain.Album) *errs.AppErrs {
	sqlstmt := "UPDATE albums SET title = ?, artist = ?, price = ? WHERE id = ?"
	result, err := a.db.Exec(sqlstmt, album.Title, album.Artist, album.Price, album.ID)

	if err != nil {
		fmt.Println("Can not connect to SQL Server.", err.Error())
		return errs.NewServerError("Server Internal Error")
	}

	rowCount, err := result.RowsAffected()

	if err != nil {
		fmt.Println("Server Get RowsAffected Error.", err.Error())
		return errs.NewServerError("Server Internal Error")
	}

	if rowCount == 0 {
		fmt.Println("No rows affected.")
		return errs.NewNotFoundError()
	}

	return nil
}

func (a *AlbumMySQL) Delete(id int) *errs.AppErrs {
	sqlstmt := "DELETE FROM albums WHERE id = ?"
	result, err := a.db.Exec(sqlstmt, id)

	if err != nil {
		fmt.Println("Can not connect to SQL Server.", err.Error())
		return errs.NewServerError("Server Internal Error")
	}

	rowCount, err := result.RowsAffected()

	if err != nil {
		fmt.Println("Server Get RowsAffected Error.", err.Error())
		return errs.NewServerError("Server Internal Error")
	}

	if rowCount == 0 {
		fmt.Println("No rows affected.")
		return errs.NewNotFoundError()
	}

	return nil
}
