#include <Havoc.h>

auto HavocClient::eventDispatch(
    const json& event
) -> void {
    auto type = std::string();
    auto data = json();

    if ( ! event.contains( "type" ) ) {
        spdlog::debug( "invalid event: {}", event.dump() );
        return;
    }

    if ( ! event.contains( "data" ) ) {
        spdlog::debug( "invalid event: {}", event.dump() );
        return;
    }

    type = event[ "type" ].get<std::string>();
    data = event[ "data" ].get<json>();

    if ( type == Event::user::login )
    {
        if ( data.empty() ) {
            spdlog::error( "user::login: invalid package (data emtpy)" );
            return;
        }
    }
    else if ( type == Event::user::logout )
    {
        if ( data.empty() ) {
            spdlog::error( "user::logout: invalid package (data emtpy)" );
            return;
        }
    }
    else if ( type == Event::user::message )
    {

    }
    else if ( type == Event::listener::add )
    {
        if ( data.empty() ) {
            spdlog::error( "listener::register: invalid package (data emtpy)" );
            return;
        }

        MainWindows->PageListener->Protocols.push_back( data );
    }
    else if ( type == Event::listener::start )
    {
        if ( data.empty() ) {
            spdlog::error( "Event::listener::start: invalid package (data emtpy)" );
            return;
        }

        MainWindows->PageListener->addListener( data );
    }
    else if ( type == Event::listener::edit )
    {

    }
    else if ( type == Event::listener::stop )
    {

    }
    else if ( type == Event::listener::status )
    {

    }
    else if ( type == Event::listener::log )
    {
        auto name = std::string();
        auto log  = std::string();

        if ( data.empty() ) {
            spdlog::error( "Event::listener::log: invalid package (data emtpy)" );
            return;
        }

        if ( data.contains( "name" ) ) {
            if ( data[ "name" ].is_string() ) {
                name = data[ "name" ].get<std::string>();
            } else {
                spdlog::error( "invalid listener log: \"name\" is not string" );
                return;
            }
        } else {
            spdlog::error( "invalid listener log: \"name\" is not found" );
            return;
        }

        if ( data.contains( "log" ) ) {
            if ( data[ "log" ].is_string() ) {
                log = data[ "log" ].get<std::string>();
            } else {
                spdlog::error( "invalid listener log: \"log\" is not string" );
                return;
            }
        } else {
            spdlog::error( "invalid listener log: \"log\" is not found" );
            return;
        }

        MainWindows->PageListener->addListenerLog( name, log );
    }
    else if ( type == Event::agent::add )
    {

    }
    else if ( type == Event::agent::initialize )
    {

    }
    else if ( type == Event::agent::callback )
    {

    }
    else if ( type == Event::agent::console )
    {

    }
    else if ( type == Event::agent::input )
    {

    }
    else if ( type == Event::agent::status )
    {

    }
    else if ( type == Event::agent::remove )
    {

    } else {
        spdlog::debug( "invalid event: {} not found", type );
    }

}