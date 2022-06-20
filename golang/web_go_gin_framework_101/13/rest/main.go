package main

import (
	"database/sql"
	"fmt"

	"github.com/monitor-cmr/web-w-go/router"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db := MysqlConn("172.17.0.2", 3306, "root", "my-secret-pw", "MYSQLTEST")
	defer db.Close()

	// test connection
	err := db.Ping()

	if err != nil {
		panic(err)
	}

	router := router.Router(db)  // get gin.Engine from the router/route.go
	router.Run(":8080")  // run app
}


func MysqlConn(host string, port int64, username, password, dbname string) *sql.DB {
	dbSource := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8", username, password, host, port, dbname)

	dbConn, err := sql.Open("mysql", dbSource)

	if err != nil {
		fmt.Println(err)
		panic(err)
	}

	return dbConn
}